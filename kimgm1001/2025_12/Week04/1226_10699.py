def main():

    from datetime import datetime, timedelta

    now = datetime.utcnow() + timedelta(hours=9)

    print(now.strftime("%Y-%m-%d"))

if __name__ == '__main__':
    main()