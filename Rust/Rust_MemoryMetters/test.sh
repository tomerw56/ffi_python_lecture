rustc memory-cache.rs
echo linear
time ./memory-cache linear 1000000
echo -e "perf"
perf stat -e instructions,cache-misses ./memory-cache linear 1000000

echo random
time ./memory-cache random 1000000
echo -e "perf"
perf stat -e instructions,cache-misses ./memory-cache random 1000000

