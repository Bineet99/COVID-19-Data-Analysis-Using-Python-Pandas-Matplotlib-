import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\binee\OneDrive\Documents\CovidData.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Active'] = df['Confirmed'] - (df['Recovered'] + df['Deceased'])
latest_date = df['Date'].max()
latest_data = df[df['Date'] == latest_date]

#Ask user for a state name
state = input("Enter the state name: ")

# Filter data for selected state
state_data = latest_data[latest_data['State'].str.lower() == state.lower()]

# Check if state data is available and plot pie chart
if not state_data.empty:
    confirmed = state_data['Confirmed'].values[0]
    recovered = state_data['Recovered'].values[0]
    deceased = state_data['Deceased'].values[0]
    active = state_data['Active'].values[0]
    values = [active, recovered, deceased]
    labels = ['Active', 'Recovered', 'Deceased']
    colors = ['orange', 'green', 'red']
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title(f'COVID-19 Case Distribution in {state.title()} ({latest_date.date()})')
    plt.axis('equal')
    plt.show()

    #Print state summary
    summary = state_data[['State', 'Confirmed', 'Recovered', 'Deceased', 'Active']]
    print(f"\nCOVID-19 Data for {state.title()} on {latest_date.date()}:\n")
    print(summary.to_string(index=False))	
else:
    print("State not found or no data available.")
# India cases
total_confirmed = latest_data['Confirmed'].sum()
total_recovered = latest_data['Recovered'].sum()
total_deceased = latest_data['Deceased'].sum()
total_active = latest_data['Active'].sum()

print(f"\nIn COVID-19 Summary for India on {latest_date.date()}:\n")
print(f"{'Confirmed':<10} {'Recovered':<10} {'Deceased':<10} {'Active':<10}")
print("-" * 47)
print(f"{total_confirmed:<10} {total_recovered:<10} {total_deceased:<10} {total_active:<10}")



