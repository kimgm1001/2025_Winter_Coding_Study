from datetime import datetime, timedelta, timezone
def main():
    s = timezone(timedelta(hours = 9))
    t = datetime.now(s)
    print(t.strftime('%Y-%m-%d'))

if __name__ == '__main__':
    main()