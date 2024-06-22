echo release
<python> -m timeit "import rustimport.import_hook;rustimport.settings.compile_release_binaries = True;from rustfib import fibonacci;fibonacci(50)"
