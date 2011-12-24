# This file will be copied to ~/.emscripten if that file doesn't exist. Or, this is that copy.
# IMPORTANT: Edit the *copy* with the right paths!

EMSCRIPTEN_ROOT = os.path.expanduser('~/Dev/emscripten') # this helps projects using emscripten find it

LLVM_ROOT = os.path.expanduser('~/Dev/llvm-3.0/cbuild/bin')

#Variables set up to tell the computer about dragonegg. Not needed if
#there is no Fortran involved in your project. 
GCC_DRAGON= os.path.expanduser('~/bin/gcc-4.6')
DRAGONEGG = os.path.expanduser('~/dev/dragonegg.so')

# See below for notes on which JS engine(s) you need
NODE_JS = 'node'
SPIDERMONKEY_ENGINE = [os.path.expanduser('~/Dev/mozilla-central/js/src/js'), '-m', '-n']
V8_ENGINE = os.path.expanduser('~/Dev/v8/d8')

CLOSURE_COMPILER = os.path.expanduser('~/Dev/closure-compiler/compiler.jar') # optional (needed for the benchmarks)

TEMP_DIR = '/tmp'


########################################################################################################


# Pick the JS engine to use for running the compiler. This engine must exist, or
# nothing can be compiled.
#
# Recommendation: If you already have node installed, use that. Otherwise, build v8 or
#                 spidermonkey from source. Any of these three is fine, as long as it's
#                 a recent version (especially for v8 and spidermonkey).

COMPILER_ENGINE = NODE_JS
#COMPILER_ENGINE = V8_ENGINE
#COMPILER_ENGINE = SPIDERMONKEY_ENGINE


# All JS engines to use when running the automatic tests. Not all the engines in this list
# must exist (if they don't, they will be skipped in the test runner).
#
# Recommendation: If you already have node installed, use that. If you can, also build
#                 spidermonkey from source as well to get more test coverage (node can't
#                 run all the tests due to node issue 1669). v8 is currently not recommended
#                 here because of v8 issue 1822.

JS_ENGINES = [NODE_JS, SPIDERMONKEY_ENGINE]

