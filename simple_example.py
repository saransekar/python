import argparse

def a(arg1, arg2, **kwargs):
    print arguments.arg1+3
    print arguments.arg2*4

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.set_defaults(method = a)
        parser.add_argument('arg1', type = int)
        parser.add_argument('arg2', type = int)

        arguments = parser.parse_args()
        arguments.method(**vars(arguments))
        

