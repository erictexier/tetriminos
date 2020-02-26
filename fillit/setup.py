# python3 setup.py build_ext --inplace
from distutils.core import setup, Extension
sources = ["fillit.c",
            "grid_utils.c",
            "grid_utils2.c",
            "resolve_iter.c",
            "tetrino_utils.c",
            "tetrino_utils2.c",
            "get_next_line.c",
            "tetrino_bound.c",
            "tetrino_utils1.c"]
def main():
    setup(  name = "tetrino",
            version = "1.0.0",
            description="Python with tetrino function",
            author="Eric",
            author_email="erictexier@gmail.com",
            ext_modules=[Extension(	"tetrino", ["tetrinomodule.c"] + sources, 
                    				include_dirs = ['./libft'], 
                    				library_dirs = ['./libft/'], 
                    				libraries = ['ft'],
                                    )])

if __name__ == "__main__":
    main()
