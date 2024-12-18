bytes = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".split('\n')

g = list()

n = 7

LARGE = True
if LARGE:
    n = 71
    bytes = """24,11
6,19
5,16
52,41
63,48
61,30
1,8
34,17
59,53
37,65
32,57
17,19
21,58
17,5
66,53
7,19
43,66
55,45
30,59
12,13
5,26
42,57
15,31
35,66
21,27
55,44
60,65
4,19
65,65
9,13
19,12
69,49
57,65
69,66
3,1
58,65
15,29
39,55
13,28
35,67
25,5
13,27
63,43
25,1
38,17
19,3
64,65
50,57
49,69
59,48
69,55
52,65
21,17
59,43
31,56
53,35
30,65
14,31
57,54
49,58
16,29
61,29
19,2
39,69
17,14
13,17
32,13
18,27
56,35
64,43
63,34
23,23
21,25
14,21
65,35
9,19
6,15
65,39
23,5
57,31
1,29
25,47
69,47
17,27
19,11
68,33
49,47
25,12
4,17
26,57
1,25
57,37
35,10
17,7
19,1
53,37
52,51
33,63
59,67
63,62
57,39
5,36
46,65
23,21
57,57
59,57
7,32
7,5
7,35
65,50
15,24
63,47
49,46
1,24
27,15
15,12
69,45
47,49
45,61
43,59
59,62
67,47
65,57
29,15
50,67
60,49
23,25
41,60
11,36
67,44
57,61
16,5
35,61
25,65
7,26
69,69
16,1
15,5
9,7
8,31
19,21
60,27
51,63
52,67
47,68
53,69
57,63
15,4
6,41
49,56
25,16
69,37
48,69
31,3
62,67
64,55
2,31
29,60
57,44
33,6
66,37
44,51
57,43
4,41
60,61
16,17
13,31
7,3
31,7
51,41
64,39
18,9
1,36
39,59
59,41
28,7
37,62
27,3
65,69
9,27
6,5
17,16
9,3
41,63
10,25
13,29
61,55
13,23
53,63
2,29
53,53
5,32
62,33
26,61
67,61
9,28
9,18
37,68
26,7
28,63
27,2
69,53
3,5
65,51
1,6
37,16
66,45
63,64
23,27
58,37
6,35
47,67
7,29
50,69
67,37
65,53
9,38
59,37
7,17
39,65
17,21
5,5
53,56
31,10
7,7
56,55
25,58
19,25
14,29
5,7
9,5
47,63
33,70
4,37
26,59
61,42
51,69
11,39
15,19
2,19
5,20
58,39
65,63
61,47
69,31
1,23
25,25
48,65
65,24
21,23
27,23
69,42
62,63
61,52
25,13
9,21
25,54
39,68
4,23
13,32
11,27
27,65
5,30
67,64
55,28
8,1
63,45
3,13
63,63
29,65
18,5
1,13
68,29
61,51
33,65
1,21
57,52
3,8
22,7
23,59
37,64
23,67
68,51
61,31
55,57
65,32
59,61
7,44
25,19
3,37
2,37
1,18
7,33
47,43
45,66
19,18
67,30
53,31
13,22
28,17
12,5
67,66
33,61
58,47
43,67
28,65
5,11
17,2
61,37
28,11
0,29
7,24
65,60
55,55
53,59
23,1
21,9
33,59
63,61
9,1
58,33
5,14
63,67
67,67
60,45
70,35
17,23
51,44
19,14
18,31
55,35
55,69
68,31
67,41
65,33
50,47
18,3
59,32
2,33
50,37
29,11
30,67
69,65
62,27
54,63
17,29
23,7
12,21
9,33
44,59
21,67
30,51
57,33
61,67
34,61
49,60
66,39
3,46
49,64
23,65
17,13
53,47
18,19
56,41
67,40
47,69
67,49
2,3
59,49
12,15
57,34
51,55
37,55
8,5
68,59
53,33
24,33
4,13
59,50
55,47
28,67
15,27
24,25
21,13
2,39
15,1
23,4
31,68
67,51
42,59
64,29
69,59
9,31
7,25
22,63
68,45
53,36
28,57
40,59
10,5
49,50
47,57
31,17
1,26
5,27
0,33
58,45
45,65
39,60
43,65
51,31
11,10
57,58
62,29
23,63
63,51
1,17
69,62
66,49
63,33
55,39
70,45
16,23
62,49
55,43
9,15
69,63
21,15
35,63
21,3
21,20
1,37
27,9
69,25
27,0
6,47
57,40
23,66
36,67
61,63
63,41
59,33
45,58
61,54
45,52
1,35
39,13
5,35
24,7
27,57
35,9
7,27
45,63
55,54
63,49
67,62
22,3
63,55
22,67
69,36
41,59
29,69
37,67
5,10
55,33
9,20
65,31
57,51
43,64
51,65
70,63
63,40
59,31
67,59
3,31
16,33
41,61
35,69
55,61
6,3
15,26
51,40
65,43
63,46
47,65
57,32
65,41
61,43
43,56
5,22
54,67
27,11
53,34
26,5
57,47
51,47
17,11
14,1
49,66
19,20
44,63
27,5
5,33
67,43
61,53
59,28
61,61
37,63
60,35
3,29
29,9
50,43
63,31
13,26
13,3
38,55
30,9
21,61
61,44
53,55
9,29
10,23
59,36
27,62
59,27
17,3
19,58
55,30
9,17
4,33
65,54
5,9
40,63
50,61
68,57
34,63
3,27
59,45
27,12
65,47
31,65
25,67
13,15
33,13
70,59
4,3
45,59
31,60
25,7
32,61
31,0
67,56
2,21
3,25
67,31
25,3
61,35
30,23
68,69
63,52
63,59
62,37
59,56
7,31
20,5
65,22
53,46
3,21
17,6
59,38
9,9
53,57
58,67
57,68
1,12
23,9
32,69
69,35
11,2
51,62
29,61
25,57
37,52
15,65
11,3
3,39
38,61
1,39
52,59
56,63
59,35
45,69
53,54
5,15
17,10
16,21
29,10
15,39
3,35
29,19
3,11
7,23
54,31
63,56
69,52
31,61
53,67
65,62
54,49
15,25
27,7
59,42
65,67
63,58
65,29
27,4
38,65
69,56
63,57
5,6
45,70
45,57
3,9
67,35
57,55
61,38
51,67
1,27
19,27
1,9
63,68
19,22
64,37
19,9
15,18
29,57
12,29
37,69
60,67
19,13
1,43
59,55
21,7
1,4
56,37
48,53
3,15
19,26
10,1
61,64
61,59
16,25
25,10
2,11
49,67
24,57
61,33
65,58
51,34
59,51
61,46
25,15
47,59
3,7
22,13
29,16
67,57
65,37
3,40
25,9
33,7
17,12
62,35
15,20
61,60
51,61
46,63
65,66
57,53
64,47
32,65
8,17
29,1
55,34
58,63
9,25
49,49
5,1
21,24
59,58
25,23
7,15
63,60
11,26
15,8
25,59
55,42
11,5
27,1
46,47
29,67
20,13
20,25
14,5
49,55
29,55
2,15
55,65
61,57
3,3
47,61
26,15
19,7
67,36
69,61
47,51
36,69
40,69
31,57
4,31
19,57
19,5
19,23
55,41
69,68
49,63
27,13
27,59
66,59
39,67
54,51
63,44
5,28
8,39
32,7
65,42
35,60
13,35
51,51
57,45
63,53
55,68
21,2
45,60
66,47
29,12
3,10
51,59
39,66
8,23
9,22
15,17
57,50
53,39
2,43
53,44
55,66
52,57
7,2
13,24
1,33
8,13
29,58
23,11
59,65
51,43
19,15
59,52
6,1
24,55
30,15
51,68
40,65
24,61
35,65
53,52
67,45
1,1
35,64
4,1
25,2
19,66
33,9
55,60
24,17
53,51
25,6
29,8
1,5
3,23
18,23
31,1
67,69
61,49
61,56
63,70
11,21
61,26
51,35
17,28
17,15
19,17
36,55
21,11
25,11
65,30
8,27
53,45
22,57
59,29
59,54
7,43
6,29
55,62
63,69
51,36
57,56
7,1
20,29
47,58
3,45
43,53
65,55
55,59
3,4
66,33
62,53
20,21
23,13
5,42
12,7
10,37
51,33
5,31
59,63
63,32
11,19
22,53
3,17
67,52
59,59
17,17
11,30
44,55
61,39
3,6
26,9
68,49
55,46
49,65
15,3
13,25
17,1
25,55
69,39
27,63
25,61
27,22
14,7
6,23
57,59
53,65
1,19
7,10
12,35
5,3
36,61
65,26
55,51
60,31
1,42
64,35
56,49
13,5
5,12
21,1
68,39
5,29
21,16
43,69
53,70
5,21
13,21
57,41
23,60
3,34
43,62
47,55
23,57
1,41
49,61
22,11
17,25
67,55
23,18
5,25
19,16
69,54
10,15
67,42
63,37
59,39
57,49
67,53
17,8
36,47
20,9
23,3
24,9
63,29
55,37
9,4
31,67
31,69
24,65
29,7
1,7
39,63
1,38
3,41
33,57
26,65
69,33
41,57
34,67
24,3
53,64
13,11
34,23
12,3
62,41
0,15
45,68
2,17
5,37
63,39
37,58
51,54
66,63
13,2
1,22
61,40
12,33
3,19
67,24
39,51
22,23
17,65
11,31
5,13
7,37
57,67
7,34
19,19
45,67
56,65
57,60
51,64
51,49
23,15
31,59
24,15
29,13
46,61
27,29
23,0
37,61
33,69
48,61
13,19
40,55
22,9
55,58
24,23
21,4
15,21
1,14
53,38
61,27
22,21
11,1
53,32
51,39
23,14
57,35
69,57
21,59
61,58
55,48
18,63
43,61
31,9
41,65
65,59
65,61
1,31
65,68
5,8
69,48
43,68
27,61
27,14
51,45
69,51
64,51
52,47
47,54
33,67
11,25
68,47
59,47
13,1
27,67
20,7
67,34
1,0
55,31
15,23
69,67
21,5
34,57
9,30
65,45
47,56
26,67
65,12
13,43
39,37
1,55
41,11
7,41
17,62
67,3
32,21
7,48
55,53
43,34
41,48
69,1
43,63
22,29
67,23
68,9
9,49
39,32
31,31
19,30
17,59
27,45
51,9
11,59
57,21
67,5
51,1
18,59
53,13
33,66
39,53
41,39
37,10
19,39
13,12
62,13
49,15
16,39
33,15
21,52
34,55
19,67
21,39
31,52
65,13
11,18
51,15
67,7
46,29
46,3
27,68
43,6
2,67
36,49
59,11
13,16
52,7
37,27
55,25
27,50
47,7
69,24
35,43
17,37
39,18
35,6
34,45
63,6
13,44
3,50
7,49
3,69
38,31
53,42
41,50
43,57
33,47
15,10
29,42
0,55
37,17
32,49
21,31
22,31
58,17
51,13
15,47
5,55
39,20
11,65
51,23
19,60
51,7
37,14
15,51
56,21
2,55
15,66
35,1
37,53
59,19
65,15
26,25
54,5
67,10
52,25
65,19
25,39
37,2
25,28
12,47
7,69
47,23
17,68
0,45
55,13
15,55
63,19
61,70
13,13
27,44
56,13
67,33
9,46
3,54
33,4
40,3
51,16
43,25
15,11
33,8
51,10
10,45
11,28
46,23
41,28
50,17
49,42
43,5
55,19
59,9
19,63
15,57
63,35
63,27
24,39
3,63
13,41
35,41
49,1
16,37
47,5
35,53
45,10
34,13
67,25
37,13
43,49
11,54
47,47
45,29
5,70
64,7
13,57
27,31
23,43
35,33
29,39
31,53
39,27
9,69
39,41
23,28
23,29
39,61
35,31
12,39
43,48
65,27
41,5
18,51
39,29
58,43
37,44
42,67
50,53
17,45
35,29
42,25
42,63
11,13
33,23
29,27
29,21
45,27
59,3
16,53
69,40
23,55
43,15
43,27
53,25
41,55
7,11
44,25
41,47
24,69
30,25
40,35
25,49
35,35
9,6
57,25
20,41
9,63
32,43
46,5
4,57
54,11
18,35
21,70
15,14
14,49
51,3
54,23
30,29
1,64
49,7
5,17
53,23
4,67
57,17
27,27
30,1
17,67
41,9
57,26
61,9
9,65
35,3
65,5
65,25
31,22
29,45
42,41
48,7
39,6
41,30
15,33
21,35
35,39
42,9
53,3
32,39
24,49
45,21
25,69
6,63
3,43
47,35
41,12
43,47
33,41
53,9
3,67
13,10
9,51
7,47
61,6
63,8
54,39
29,32
29,70
49,37
8,35
11,53
21,55
63,20
23,17
31,28
61,13
53,1
21,64
52,13
30,55
45,50
11,35
44,5
67,15
39,3
61,1
38,33
19,68
23,49
37,29
60,21
17,54
49,18
39,24
15,41
64,9
68,17
60,25
36,15
19,54
37,43
12,41
7,13
33,31
22,47
17,52
33,25
55,24
25,46
19,38
7,63
24,43
47,41
69,11
47,11
36,19
61,16
35,18
37,23
36,41
37,36
66,9
67,65
26,43
34,35
13,56
57,5
37,11
7,65
68,13
57,13
24,37
4,25
30,45
25,21
45,9
57,11
37,19
52,9
9,11
67,1
15,69
27,53
55,17
39,22
23,61
28,27
41,21
49,21
46,7
33,19
42,5
49,5
28,55
15,62
1,58
17,55
0,69
54,27
13,61
38,27
30,35
49,25
6,61
11,23
61,2
68,27
68,7
19,32
53,49
31,30
17,63
46,33
35,55
56,9
19,61
39,48
57,29
47,37
11,62
47,38
49,13
38,57
42,33
60,11
29,25
57,9
34,47
69,21
38,43
10,51
43,1
34,39
25,33
53,15
51,22
45,47
26,35
3,66
63,23
63,18
33,49
17,41
41,49
45,15
29,38
60,5
61,8
15,45
47,31
37,5
55,15
8,47
31,45
44,27
13,68
55,4
68,1
55,2
49,32
35,45
47,16
45,5
12,49
64,27
31,41
15,43
24,63
15,56
65,21
55,1
67,68
19,44
59,1
13,67
25,41
11,29
65,1
67,14
15,7
56,15
27,51
27,49
55,49
17,35
11,60
15,67
53,5
25,51
43,7
7,54
37,12
43,35
17,39
50,7
49,3
45,43
49,34
16,43
51,29
33,27
17,47
9,16
69,7
67,9
20,67
5,53
11,45
25,63
33,2
21,37
48,1
44,33
41,0
16,49
59,17
3,68
39,26
23,31
7,66
45,7
36,39
19,50
67,63
50,25
20,49
44,29
30,19
21,33
29,2
63,4
34,41
1,11
49,35
63,22
37,37
62,19
43,11
63,3
12,63
49,33
41,1
36,51
31,13
42,53
37,39
51,24
59,22
59,15
3,51
39,11
68,21
31,11
49,36
69,17
41,18
36,43
27,43
27,35
21,51
33,51
37,54
13,45
38,47
47,27
67,19
11,41
1,63
53,14
57,24
6,39
36,31
47,12
69,4
24,31
1,53
26,39
44,17
21,26
65,0
61,10
3,57
33,38
63,13
27,33
5,61
1,59
14,45
67,2
47,40
36,23
1,48
51,27
21,63
7,57
43,19
30,47
37,22
2,27
5,66
23,42
69,15
39,23
69,5
31,25
51,25
29,51
27,38
1,67
48,29
43,43
3,53
31,23
23,44
57,19
11,66
47,44
21,48
69,20
20,37
42,69
15,58
32,3
10,13
22,61
51,30
9,55
19,41
19,43
23,45
25,37
11,55
15,16
9,39
21,34
37,33
19,51
37,47
43,36
5,47
21,56
27,55
52,19
60,19
18,45
37,20
44,41
57,30
34,53
18,39
28,49
61,17
55,29
35,52
36,37
39,12
69,22
7,39
18,33
45,30
23,37
60,17
66,1
45,31
47,21
5,67
21,53
1,62
41,14
41,17
41,35
59,23
19,31
23,34
63,15
41,51
34,21
37,8
14,37
26,55
31,42
67,21
35,15
15,37
61,21
47,50
49,57
41,3
49,8
57,22
42,21
63,1
25,53
40,5
15,34
33,33
47,39
53,17
13,55
55,16
57,3
21,42
59,24
59,14
57,1
52,29
65,11
5,63
39,1
37,4
57,69
67,11
5,39
65,7
19,40
29,52
11,8
34,19
19,29
17,33
50,27
61,25
41,41
15,15
21,69
33,53
8,65
11,67
53,43
25,20
48,11
19,53
41,23
14,61
36,1
47,26
45,37
11,44
9,12
43,13
23,36
31,27
65,9
20,35
41,19
45,48
28,41
41,44
39,49
67,6
43,54
46,35
69,3
29,35
31,29
69,19
56,19
34,43
35,21
11,61
36,35
17,9
27,21
13,39
17,53
28,45
14,51
39,10
61,41
48,15
48,13
9,68
55,6
27,34
70,29
45,13
16,45
48,27
9,61
31,33
39,5
33,10
63,24
15,64
58,19
45,38
31,44
15,53
53,60
15,48
52,49
53,19
63,17
11,47
34,9
22,51
7,36
27,69
19,35
11,57
59,69
15,9
33,50
12,65
27,26
46,37
63,65
25,35
1,69
36,33
69,43
13,63
33,36
44,15
61,11
35,13
5,69
5,60
3,48
59,25
65,14
7,62
25,32
49,40
43,9
49,39
33,58
38,9
55,3
51,6
55,23
13,7
55,9
1,52
67,13
41,22
28,31
41,7
5,49
40,37
31,51
49,48
17,57
1,3
29,4
19,45
34,49
53,11
41,33
58,7
29,53
9,54
39,47
39,9
51,57
43,18
50,11
61,12
19,65
42,37
7,20
45,42
47,20
29,41
35,5
51,50
21,46
42,15
5,56
51,32
31,36
39,33
13,38
14,55
25,48
39,15
53,2
2,25
13,18
29,47
26,53
40,45
45,20
7,59
49,29
32,33
19,47
47,48
2,47
27,28
44,39
29,63
45,23
13,69
51,17
39,45
49,9
43,44
48,21
39,39
9,50
35,23
48,9
55,11
43,31
5,52
31,5
17,42
28,21
9,59
51,53
34,3
15,49
29,43
29,59
59,0
21,32
28,19
1,45
35,7
25,27
11,52
3,65
20,63
30,5
53,29
5,19
49,11
11,33
39,7
67,16
23,53
39,34
26,19
17,50
26,49
34,27
55,26
52,3
47,29
39,14
57,27
43,3
13,53
9,56
57,23
33,46
12,55
1,61
9,47
3,33
7,58
25,43
43,45
54,13
33,17
53,21
33,55
49,59
20,53
5,57
21,49
64,19
3,47
21,43
9,37
47,13
30,63
40,9
37,3
17,70
33,45
37,45
70,15
48,23
1,65
36,7
45,39
56,11
51,11
13,37
27,39
10,47
19,46
25,17
19,56
10,41
33,5
51,0
17,61
12,51
62,23
59,6
9,67
27,17
24,21
44,3
16,47
7,40
7,61
35,19
69,27
65,23
14,53
61,5
5,41
46,55
39,46
19,69
23,39
9,23
29,17
0,51
31,35
51,38
61,3
39,35
41,67
55,7
22,41
41,15
45,55
27,47
37,57
51,5
15,42
7,68
48,19
44,9
34,29
1,47
4,59
57,15
39,21
33,1
35,25
37,35
49,53
10,57
24,45
57,2
16,59
41,8
47,2
53,27
21,45
67,17
39,50
14,35
51,14
60,3
66,19
11,49
33,30
43,41
55,63
7,51
37,41
36,27
43,23
37,7
27,32
29,49
44,23
9,53
39,43
33,35
9,60
37,1
25,40
25,31
66,21
33,14
47,15
63,11
1,57
38,29
69,29
13,51
9,57
33,29
3,59
3,55
43,46
66,13
30,39
3,64
55,67
43,37
1,51
57,16
41,25
9,62
58,13
9,42
32,25
10,9
44,19
6,57
23,50
58,11
25,29
37,25
64,3
40,25
31,21
33,24
21,29
37,24
57,28
40,41
33,39
9,41
50,3
27,37
61,23
31,26
61,69
37,49
54,9
33,28
49,27
41,32
35,57
43,21
59,13
37,9
25,45
43,39
31,15
67,27
13,47
11,7
49,43
7,70
21,21
11,17
41,31
29,5
27,41
45,53
41,37
23,69
43,29
32,41
47,33
59,7
17,69
44,45
42,1
43,42
70,9
51,28
19,59
57,7
49,52
13,60
13,9
41,2
42,31
54,59
41,29
47,30
63,7
37,15
49,23
17,56
45,19
53,41
53,61
26,41
51,37
36,29
9,35
11,63
6,53
15,35
27,48
29,33
62,1
55,0
47,9
21,19
61,19
45,11
33,37
13,33
5,43
8,53
7,45
23,68
5,50
67,4
10,63
7,55
51,21
69,26
35,17
64,11
7,8
55,5
48,3
3,49
5,65
23,26
3,61
29,40
47,19
27,36
21,47
45,8
35,37
21,18
38,51
51,4
55,27
65,17
31,32
29,34
67,39
45,41
55,40
58,21
17,49
27,25
66,5
66,25
49,17
31,19
20,61
47,1
41,16
17,43
40,29
17,51
61,15
22,39
12,69
67,29
36,57
15,61
46,45
53,7
5,23
27,30
41,45
39,25
64,17
8,9
32,19
33,11
33,43
5,51
50,13
59,21
35,49
35,59
33,21
1,49
37,31
39,17
9,45
11,43
5,45
26,23
29,23
53,20
11,70
45,35
61,45
11,51
46,17
54,19
1,60
29,37
57,4
9,43
41,46
5,59
61,14
36,5
16,63
41,27
40,53
67,18
47,25
19,49
38,41
45,1
31,49
35,47
47,24
49,19
22,37
14,67
3,62
63,5
7,21
13,58
11,69
46,27
43,55
15,59
21,57
38,37
25,52
17,36
30,21
19,37
23,33
8,59
39,19
8,51
49,41
31,14
2,57
45,25
35,51
15,13
39,4
47,45
3,52
11,58
70,5
32,63
31,63
54,17
25,30
41,13
11,11
23,35
43,12
15,63
10,67
11,40
63,16
69,12
10,33
63,21
63,9
19,55
41,38
49,31
23,41
48,43
38,1
58,69
62,11
13,14
48,39
23,19
35,12
12,43
5,44
34,33
43,17
50,21
47,17
35,27
61,65
21,65
47,32
40,57
44,13
32,47
43,33
27,19
42,11
45,51
31,43
31,47
23,51
29,31
13,49
35,11
69,9
7,9
13,65
69,23
41,43
28,53
30,17
37,59
8,43
55,8
58,9
29,29
6,49
14,41
31,39
33,16
29,3
53,26
65,3
11,9
43,51
3,44
49,45
43,24
15,68
11,20
37,51
69,41
13,64
19,33
45,33
63,25
21,41
39,40
5,46
33,3
23,47
58,3
42,51
20,45
41,53
32,53
37,21
47,3
59,5
1,15
39,31
39,38
44,1
53,22
45,17
7,64
48,35
46,13
16,31
11,37
65,49
61,7
41,69
51,19
48,5
31,37
45,45
31,55
17,31
45,49
7,67
30,49
49,51
11,15
3,60
7,53
47,53
13,59
39,57
45,22
45,3
35,26
41,20
55,21
69,13
62,3
18,65
62,65
28,52
15,52
25,70
8,7
20,30
50,59
1,44
15,36
20,15
64,4
56,53
34,40
50,58
34,38
1,54
24,62
60,60
2,40
3,14
57,8
11,6
0,7
54,12
27,66
11,38
32,66
4,62
60,52
54,24
20,38
44,24
61,20
14,12
58,29
68,23
65,16
68,36
42,61
8,67
68,62
50,33
0,39
12,26
60,16
20,48
55,18
14,10
36,40
62,6
52,15
41,42
47,46
66,12
35,32
40,60
55,14
32,55
30,11
32,17
54,55
67,48
24,32
65,34
55,70
39,42
14,46
12,8
32,9
63,28
24,64
34,69
22,18
50,34
60,70
16,58
12,19
68,54
6,54
69,44
42,43
39,56
70,38
12,68
38,42
0,19
13,4
16,2
27,24
12,45
18,40
38,32
46,26
16,68
11,4
52,60
64,10
10,65
7,56
0,54
7,42
60,34
3,18
70,8
3,56
17,32
42,66
14,54
56,60
37,40
5,40
15,54
21,66
46,36
68,53
12,64
6,6
50,32
4,6
4,40
70,43
68,42
51,20
70,2
44,40
0,38
32,16
8,52
44,26
10,44
2,50
70,18
56,16
36,70
62,17
37,32
22,45
3,20
63,38
37,42
13,54
34,42
48,36
22,5
2,48
10,43
18,1
48,32
38,44
2,49
40,49
22,43
4,61
70,22
3,22
63,0
0,42
2,38
10,59
32,54
3,24
52,23
14,34
34,65
68,20
24,40
22,32
26,30
12,59
62,51
60,12
56,32
3,16
18,43
36,68
2,44
58,10
14,15
16,32
53,62
4,29
54,16
66,27
8,46
59,2
50,70
7,6
10,58
14,56
10,2
22,70
28,70
4,42
20,47
11,56
13,36
68,15
5,62
0,34
22,33
13,20
60,28
6,18
68,8
2,69
34,11
12,23
39,52
56,68
16,12
13,52
19,34
2,7
66,41
56,25
54,58
30,37
32,67
30,43
58,27
14,48
20,68
32,18
52,44
14,69
9,58
58,62
36,6
68,61
40,38
59,26
20,62
67,22
26,28
12,20
42,40
20,65
28,13
16,38
18,4
7,16
2,63
11,32
32,12
68,46
66,46
54,61
12,1
7,60
2,41
68,11
62,31
70,69
0,10
18,34
62,22
10,53
24,35
60,18
33,52
18,66
46,53
57,66
52,18
69,32
18,30
60,44
23,52
50,44
14,60
1,50
20,27
2,60
42,13
6,48
2,58
0,53
24,68
64,30
18,41
0,57
56,47
16,62
66,36
20,69
37,48
56,4
61,34
42,47
9,26
14,20
56,59
0,4
26,36
14,38
24,28
12,67
16,50
70,27
20,32
4,39
14,19
65,2
66,26
32,64
44,36
56,1
50,46
28,39
68,65
32,70
8,11
30,8
61,66
69,64
22,27
28,44
44,34
8,4
34,46
6,68
32,37
14,30
6,58
0,22
24,26
14,57
28,48
8,57
68,68
29,68
52,10
26,46
3,38
67,46
69,18
34,51
54,62
1,10
58,60
57,6
48,51
18,68
52,63
63,30
20,33
21,68
46,8
25,62
68,4
59,70
45,54
25,44
66,22
50,68
46,46
55,20
64,45
31,66
30,50
42,26
2,54
67,0
56,66
10,36
57,0
6,50
70,32
8,26
2,34
10,6
56,29
65,20
16,30
50,40
64,69
35,70
16,61
50,35
36,38
56,51
13,34
15,70
69,2
24,41
10,54
22,25
70,48
8,8
64,38
68,14
7,52
48,44
58,1
1,34
66,29
54,26
0,60
11,46
21,50
52,62
44,43
40,44
20,18
44,18
55,52
12,25
7,50
12,58
12,57
12,12
6,65
46,38
23,30
8,48
26,44
45,28
67,54
10,22
15,46
14,17
13,42
13,66
12,10
16,24
12,24
69,60
69,16
6,69
8,15
38,56
18,2
36,45
56,7
43,60
6,14
12,14
11,14
11,68
44,62
24,34
0,56
38,13
44,37
14,16
56,6
64,68
32,15
23,64
58,52
56,34
23,62
20,17
26,54
12,56
70,23
44,31
58,56
45,18
10,20
14,18
10,62
54,68
28,46
66,61
14,11
52,42
48,52
28,58
3,2
56,20
54,60
9,44
40,68
12,48
52,43
4,68
47,52
9,40
2,6
14,70
65,44
63,66
29,46
53,50
50,42
18,47
30,18
35,40
18,44
20,19
48,66
30,53
16,11
61,22
26,26
68,10
34,37
6,2
28,16
6,10
5,64
54,10
47,66
58,55
14,58
64,46
62,69
64,18
14,63
23,70
2,53
70,42
70,11
32,2
18,62
43,40
8,62
0,21
56,58
70,46
0,26
29,64
70,44
0,5
58,2
69,28
30,42
58,58
70,0
58,68
42,56
70,28
31,2
62,38
14,4
67,26
34,28
59,68
60,36
21,36
12,11
58,4
62,16
40,67
47,8
2,24
5,18
67,20
19,48
52,5
18,58
70,39
44,0
12,42
10,16
62,26
60,66
26,14
43,8
27,6
32,44
13,48
46,0
67,32
52,12
2,16
46,48
57,10
8,2
58,53
51,18
35,24
4,44
18,61
57,48
21,12
52,31
33,54
32,20
11,16
56,46
34,54
8,70
0,44
40,58
34,12
41,64
5,34
36,9
26,66
64,24
38,49
58,36
50,16
32,31
28,38
66,55
58,28
47,42
3,70
51,8
68,24
39,0
46,28
0,62
29,0
37,56
62,60
64,36
44,32
42,28
36,66
64,28
54,37
15,32
2,59
21,40
18,28
32,5
17,34
14,68
9,52
32,8
10,61
64,60
49,30
28,8
31,18
64,67
8,58
35,14
0,37
36,17
65,36
42,29
48,47
40,12
54,21
33,22
62,66
32,30
4,35
38,50
35,48
20,54
0,65
10,19
34,36
37,6
43,38
48,37
40,6
58,40
68,32
46,43
11,12
40,51
49,0
39,8
23,38
1,56
35,34
54,32
22,50
44,44
14,8
8,49
0,20
35,54
24,2
36,54
10,10
16,56
16,41
28,3
44,46
20,20
5,58
32,45
4,58
37,66
29,22
57,12
46,40
41,24
44,28
5,24
25,4
14,22
54,65
46,59
10,17
52,21
16,22
30,10
70,36
64,40
66,64
44,61
57,20
44,57
20,34
20,57
8,40
39,54
46,25
58,54
59,10
34,68
20,55
38,69
11,34
58,64
48,59
4,65
47,18
40,4
56,18
8,19
70,21
20,0
24,6
38,34
70,41
40,19
23,22
36,8
24,5
54,48
64,50
64,6
50,52
16,67
27,54
58,70
64,23
1,30
51,58
60,33
38,20
24,12
34,5
8,25
53,58
34,31
32,29
48,17
42,12
52,50
52,8
3,36
38,46
29,24
26,29
38,48
48,67
44,35
50,51
30,32
64,25
40,70
18,57
64,21
7,18
50,49
12,2
63,2
54,7
35,0
62,9
37,60
20,12
36,62
16,6
40,61
0,67
10,31
66,58
42,17
42,7
16,46
25,14
4,60
54,0
2,12
65,52
40,26
22,66
42,45
33,32
54,43
28,4
25,50
35,16
42,27
32,68
38,4
10,32
48,4
16,4
46,14
37,70
0,49
68,64
30,33
10,34
60,46
70,50
16,57
58,59
22,19
30,69
28,54
49,28
28,51
63,36
55,22
28,15
18,38
30,61
28,9
58,14
34,30
56,22
31,12
26,27
31,64
49,68
48,30
56,5
4,48
33,12
44,56
27,46
43,0
30,44
10,69
54,29
12,32
19,42
3,12
54,34
33,68
2,61
44,52
30,66
38,15
12,52
56,57
36,36
8,10
51,60
61,24
18,64
0,18
57,42
50,19
48,68
36,52
16,18
26,50
7,4
36,53
6,67
61,28
37,26
44,68
0,66
24,54
13,62
46,19
12,53
38,24
4,53
54,66
38,38
2,36
31,38
38,59
31,62
62,70
8,56
48,10
6,13
49,16
32,34
2,4
20,3
56,31
61,4
50,55
31,4
30,24
14,2
18,15
70,40
27,64
38,22
47,6
65,28
28,64
27,16
62,58
20,2
46,11
58,12
33,26
47,4
19,64
48,63
38,67
62,7
1,32
70,12
62,47
58,23
14,13
52,1
16,36
18,22
26,48
24,48
30,30
45,34
10,70
42,65
68,60
50,6
8,60
40,13
16,65
21,44
33,42
68,38
50,63
49,4
40,14
52,4
69,8
52,69
53,16
58,34
42,68
44,60
11,22
12,36
61,62
12,6
27,42
46,24
18,16
0,28
50,48
22,6
10,18
66,6
43,14
56,54
64,59
68,52
49,14
24,70
38,3
24,66
41,40
6,62
70,66
11,42
66,17
68,0
14,65
54,18
66,7
40,20
42,64
70,61
16,69
4,28
1,2
55,12
30,34
54,2
15,22
56,30
33,56
21,14
38,12
35,62
24,10
44,11
56,44
54,53
8,0
23,56
70,20
3,32
70,55
55,56
59,40""".split('\n')

for _ in range(n):
    g.append(['.'] * n)

for byte in bytes[:1024]:
    x, y = byte.split(',')
    x, y = int(x), int(y)
    g[y][x] = '#'

# for row in g:
#     print(''.join(row))

frontier = {(0, 0)}
seen = {(0, 0)}
progress = True
t = 0
from itertools import product

def neighbors(nn):
    x, y = nn
    r = set()
    for dx, dy in product([-1, 0, 1], repeat=2):
        if not((dx == 0) ^ (dy == 0)) or not (0 <= x + dx < n) or not (0 <= y + dy < n):
            continue
        if g[x + dx][y + dy] == '.':
            r.add((x + dx, y + dy))
    return r

while progress:
    if (n - 1, n - 1) in seen:
        print(t)
        break
    t += 1
    progress = False
    new_frontier = set()
    for p in frontier:
        for neighbor in neighbors(p):
            if neighbor not in seen:
                progress = True
                new_frontier.add(neighbor)
                seen.add(neighbor)
    frontier = new_frontier
