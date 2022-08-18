n = int(input())
mins, secs = divmod(n, 60)
hours, mins = divmod(mins, 60)
print(f"{hours}:{mins}:{secs}")
