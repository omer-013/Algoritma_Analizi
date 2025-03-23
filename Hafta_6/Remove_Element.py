def remove_element(arr, value):
    if value in arr: 
        arr.remove(value) 
    else:
        print("Eleman dizide bulunamadı")
    return arr