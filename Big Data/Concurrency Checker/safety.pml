bool lock = false; // The database lock
byte critical_section_count = 0; // Should never be more than 1

active [2] proctype User() {
    do
    ::  /* Try to enter critical section */
        atomic {
            !lock -> lock = true;
        }

        /* Critical Section Starts */
        critical_section_count++;
        printf("Process %d is writing to DB\n", _pid);
        
        /* ASSERTION: If count > 1, two processes are writing at once! */
        assert(critical_section_count <= 1);
        
        critical_section_count--;
        /* Critical Section Ends */

        lock = false;
    od
}
