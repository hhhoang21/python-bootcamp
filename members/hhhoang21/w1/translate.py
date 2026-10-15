"""
vector<int>& insertion_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}
"""
def insertion_sort(arr: list[int]) -> list[int]:
    """Sorts an integer list in-place using insertion sort and returns the list."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Dịch chuyển các phần tử lớn hơn key về sau
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr