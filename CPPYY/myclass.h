#ifndef MYCLASS_H
#define MYCLASS_H

class MyClass {
public:
    MyClass(int initial_value) : value(initial_value) {}
    void set_value(int new_value) { value = new_value; }
    int get_value() const { return value; }

private:
    int value;
};

#endif // MYCLASS_H