use std::env::args;
// compile with rustc memory-cache.rs
fn main() {
    // Get the first command-line argument:
    let scan_type = args().nth(1).expect(
        "Must provide scan type argument.");

    // Get the second argument, convert to an integer:
    let vector_size = args().nth(2).expect(
        "Must provide array size argument.");
    let vector_size = vector_size.parse::<usize>().expect(
        "Not an integer.");

    // Figure out an appropriate multiplier:
    let multiplier = match &*scan_type {
        "linear" => 1,
        "random" => 48271,
        _ => panic!("Unknown scan type."),
    };

    // Create 4 vectors (for our purposes, an array in
    // memory) of size vector_size, filled with zeros.
    let mut data = vec![0; vector_size];
    let mut data2 = vec![0; vector_size];
    let mut data3 = vec![0; vector_size];
    let mut data4 = vec![0; vector_size];

    // Update values in the vectors. A multiplier of 1
    // results in a linear memory scan, whereas 48271
    // will result in jumping around memory "randomly":
    let mut index = 0;
    for _ in 0..100_000_000 {
        data[index] += 1;
        data2[index] += 1;
        data3[index] += 1;
        data4[index] += 1;
        index = (multiplier * index + 1) % vector_size;
    }
}
