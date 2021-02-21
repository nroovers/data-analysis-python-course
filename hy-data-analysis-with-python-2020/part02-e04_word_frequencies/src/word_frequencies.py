#!/usr/bin/env python3

def word_frequencies(filename):
    d={}
    with open(filename, "r") as f:
        for line in f:
            for s in line.split():
                ss=s.strip("""!"#$%&'()*,-./:;?@[]_""")
                if ss in d:
                    d[ss]+=1
                else:
                    d[ss]=1
    return d

def main():
    print(word_frequencies('src/alice.txt'))

if __name__ == "__main__":
    main()
