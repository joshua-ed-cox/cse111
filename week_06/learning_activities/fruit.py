def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    # Reverse the fruit list then print it
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # Append Orange to the end of the fruit list
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    # Insert cherry before apple in the fruit list
    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(f"insert cherry: {fruit_list}")

    # remove "banana" from fruit_list and print the list
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    # pop the last element from fruit_list and print the popped element and the list
    fruit_list.pop()
    print(f"pop orange: {fruit_list}")

    # sort and print fruit_list
    fruit_list.sort
    print(f"sorted: {fruit_list}")

    # clear and print fruit_list
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

main()
    
    