static int KthSmallestElement(int[] arr, int k)
{
    if (k <= 0 || k > arr.Length){
        Console.WriteLine("Gecersiz k degeri");
    	return -1;
    }
    int[] copy = (int[])arr.Clone();
    Array.Sort(copy);

return copy[k - 1];
}   
    