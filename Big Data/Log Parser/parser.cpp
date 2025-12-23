#include <iostream>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string>
#include <fstream>


int main() {
   const char* filepath = "access.log";
   int fd = open(filepath, O_RDONLY);
   if (fd == -1) return 1;


   struct stat sb;
   fstat(fd, &sb);


   char* addr = (char*)mmap(NULL, sb.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
   std::ofstream outFile("errors.csv");


   size_t line_start = 0;
   for (size_t i = 0; i < sb.st_size; ++i) {
       if (addr[i] == '\n') {
           // Convert the current line to a string for easier searching
           std::string line(addr + line_start, i - line_start);
          
           // Look for " 404 " (with spaces to ensure it's the status code)
           if (line.find(" 404 ") != std::string::npos) {
               // The IP is the first part of the line before the first space
               size_t first_space = line.find(' ');
               if (first_space != std::string::npos) {
                   outFile << line.substr(0, first_space) << "\n";
               }
           }
           line_start = i + 1;
       }
   }


   std::cout << "Done! Parser has written found errors to errors.csv" << std::endl;
   munmap(addr, sb.st_size);
   close(fd);
   return 0;
}





