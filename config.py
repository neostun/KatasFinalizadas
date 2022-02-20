def main():
    try:
        configuration = open('config.txt')
    except PermissionError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()