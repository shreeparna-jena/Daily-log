from datetime import date

LOG = "daily_log.txt"

def write_log(today_entry, tomorrow_entry):
    today = date.today().strftime("%d-%m-%y")

    with open(LOG, "a", encoding="utf-8") as file:
        file.write(f"Date: {today}\n")
        file.write(f"Today: {today_entry}\n")
        file.write(f"Tomorrow: {tomorrow_entry}\n")
        file.write("-" * 30 + "\n")

def main():
    print("Daily Log\n")

    today_entry = input("What did you do today? ").strip()
    tomorrow_entry = input("What will you do tomorrow? ").strip()

    write_log(today_entry, tomorrow_entry)
    print("\nYour log has been saved.")

if __name__ == "__main__":
    main()
