import pandas as pd


try:
   # Read the CSV created by your C++ program
   df = pd.read_csv("errors.csv", names=["IP"])


   print("--- BIG DATA LOG ANALYSIS ---")
   print(f"Total 404 Errors Found: {len(df)}")
   print("\nTop 5 'Attacker' IPs (Most 404s):")
  
   # This is like a SQL 'GROUP BY' and 'ORDER BY'
   top_ips = df['IP'].value_counts().head(5)
   print(top_ips)


except Exception as e:
   print("No errors.csv found or file is empty. Run the C++ parser first!")





