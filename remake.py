def fdiseases(s):
    if s == "virus":
        with open("virus.txt", 'r') as f:
            ans2 = f.read()
        return ans2
    if s == "bacteria":
        with open("bacteria.txt", 'r') as f:
            ans2 = f.read()
        return ans2
    if s == "protist":
        with open("protist.txt", 'r') as f:
            ans2 = f.read()
        return ans2
    if s == "fungi":
        with open("fungi.txt", 'r') as f:
            ans2 = f.read()
        return ans2

def fbiology(t):
    if t == "disease":
        ans1 = fdiseases(subtopic)
        return ans1
    else:
        return "Subtopic not found."

while True:

    
    subject = input("Subject? (biology)_")
    topic = input("Topic? (diseases)_")
    subtopic = input("Subtopic? (virus, bacteria, protist, fungi)_")

    if subject.lower() in ['b', 'bio', 'biology']:
        ans = fbiology(topic)
        print(ans)
    else:
        print("Invalid subject.")

