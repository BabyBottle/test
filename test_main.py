import subprocess

def test_main():
    ExceptedOutput = 'Hello wworld'
    output = subprocess.Popen('./test3/hello', stdout=subprocess.PIPE)
    output_string = output.stdout.read().decode('utf-8')
    if(output_string == ExceptedOutput):
        print("Correctly print")
    else:
        assert output_string == ExceptedOutput, "[ERROR] expected output is %s, but the main.c print %s"%(ExceptedOutput, output_string)

if __name__ == "__main__":
    test_main()
