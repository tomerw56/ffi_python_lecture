// rustimport:pyo3

// PyO3 is a Rust library for writing Python extensions;
// we'll import its most commonly used APIs.
use pyo3::prelude::*;

#[pyfunction]  // ← expose the function to Python
fn fibonacci(number: u64) -> u64 {
    if number == 0 {
        return 0;
    }
    if number == 1 {
        return 1;
    }
    let mut prevprev = 0;
    let mut prev = 1;
    let mut current = 1;
    for _ in 0..(number - 1) {
        current = prevprev + prev;
        prevprev = prev;
        prev = current;
    }
    current
}
