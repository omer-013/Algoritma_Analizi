def update_element(arr, index, new_value):
    if 0 <= index < len(arr):  
        arr[index] = new_value 
    else:
        print("Geçersiz indeks") 
    return arr