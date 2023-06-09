#学习使用auto定义变量的用法。
'''
在 C++ 语言中，auto 关键字的作用是让编译器自动推断变量的类型。使用 auto 关键字定义变量时，编译器会根据变量的初始化值来推断其类型。例如：

c++
Copy code
auto a = 10;      // 推断 a 的类型为 int
auto b = 3.14;    // 推断 b 的类型为 double
auto c = "hello"; // 推断 c 的类型为 const char*
auto 关键字在 C++11 标准中被引入，可以减少代码的冗余和编写时的工作量，同时可以避免手动定义变量类型时的错误和不便。

'''