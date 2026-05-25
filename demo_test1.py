Here's the code to add two numbers in C++:

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two integers: ";
    cin >> a >> b;

    int sum = a + b;
    int product = a * b;

    cout << "Sum: " << sum << endl;
    cout << "Product: " << product << endl;

    return 0;
}
```

Explanation:

1. First, we include the necessary header files to use std::cout and std::cin for input/output.
2. Then, we create a `main` function which prompts the user to enter two integers followed by pressing Enter. We then store their values in variables `a` and `b`.
3. In the following block of code, we perform operations using arithmetic operators (`+`, `*`) between `a` and `b` (which are stored in `sum` and `product`). We also use variable names to make it easier to read and understand the code.
4. Finally, we output both values in a single line.