states = {
	"[ 1  0  0 -1  1 -1  0  0  1  0]" : {1: [(0, 4, 1)]},
	"[ 1  0  0  0  1 -1  1  0  0  0]" : {1: [(0, 4, 1), (0, 6, 3)]},
	"[-1 -1  0  0  1  1  1  0  0  0]" : {1: [(1, 1, 5)]},
	"[ 1 -1  0  0  1  1 -1  0  1  0]" : {1: [(0, 5, 2), (1, 5, 1), (1, 8, 6)]},
	"[-1 -1  0 -1  1  1  0  0  1  0]" : {1: [(1, 1, 5), (0, 3, 6)], -1: [(1, 3, 5)]},
	"[ 1 -1  0 -1  1 -1  0  0  1  1]" : {1: [(0, 9, 6)], -1: [(1, 9, 5)]},
	"[-1  0  0 -1 -1 -1  1  0  0  0]" : {-1: [(0, 4, 7), (0, 5, 8)]},
	"[ 1  0  0  0 -1  1 -1  0  0  0]" : {1: [(0, 5, 2)]},
	"[-1  0  0 -1 -1  1  0  0  0  0]" : {1: [(0, 3, 6)], -1: [(1, 3, 5), (0, 4, 7)]},
	"[ 1  0  0 -1 -1 -1  0  0  0  1]" : {-1: [(0, 9, 6), (1, 9, 5)]},
	"[ 1 -1  0  0 -1  1 -1  0  0  1]" : {1: [(0, 5, 2), (1, 5, 1)]},
	"[-1 -1  0  0 -1 -1  1  0  0  0]" : {-1: [(0, 4, 7), (0, 5, 8)]},
	"[-1 -1  0  0 -1  1  0  0  0  0]" : {-1: [(1, 1, 5), (0, 4, 7)]},
	"[ 1 -1  0  0 -1 -1  0  0  0  1]" : {-1: [(0, 9, 6), (1, 9, 5)]},
	"[-1 -1  0 -1 -1  1  0  0  0  1]" : {-1: [(1, 1, 5), (1, 3, 5), (0, 4, 7)], 1: [(0, 3, 6)]},
	"[-1 -1  0 -1  1  0  0  0  0  1]" : {-1: [(0, 3, 6)]},
	"[-1 -1  0 -1 -1  0  1  0  1  0]" : {-1: [(0, 4, 7), (1, 4, 8)]},
	"[ 1 -1  0 -1 -1  0  0  0  1  1]" : {-1: [(0, 8, 5), (1, 8, 4), (0, 9, 6)]},
	"[-1  0 -1  0  1  1 -1  0  0  0]" : {1: [(1, 2, 4)], -1: [(0, 6, 9)]},
	"[ 1  0 -1  0  1 -1 -1  0  0  1]" : {1: [(0, 4, 1), (1, 4, 2)], -1: [(1, 9, 5)]},
	"[-1 -1 -1  0  1  1 -1  0  0  1]" : {1: [(1, 1, 5), (1, 2, 4)]},
	"[ 1 -1  0  0  1 -1  1  0  0  1]" : {1: [(0, 6, 3), (1, 9, 5)]},
	"[ 1 -1  0  0 -1  0  1  0  0  1]" : {1: [(0, 6, 3)]},
	"[-1 -1 -1  0  1  0  1  0  0  1]" : {1: [(0, 2, 5), (1, 2, 4)], -1: [(1, 2, 6)]},
	"[ 1 -1 -1  0  1  0 -1  0  1  1]" : {1: [(1, 4, 2), (0, 8, 5)], -1: [(1, 8, 6)]},
	"[-1 -1 -1 -1  1  0  0  0  1  1]" : {1: [(0, 2, 5), (0, 3, 6)], -1: [(1, 2, 4)]},
	"[ 1  0  0 -1 -1  1 -1  1  0  0]" : {1: [(0, 5, 2), (1, 5, 3)]},
	"[-1  0 -1  0 -1  1  1  0  0  0]" : {1: [(1, 2, 6)], -1: [(0, 4, 7)]},
	"[ 1  0 -1  0 -1 -1  1  1  0  0]" : {1: [(0, 6, 3), (1, 6, 2)], -1: [(1, 7, 5)]},
	"[-1  0 -1 -1 -1  1  1  1  0  0]" : {1: [(1, 2, 6), (1, 3, 5)]},
	"[ 1  0 -1 -1 -1  1  0  1  0  1]" : {1: [(1, 5, 3), (0, 9, 6)]},
	"[-1  0 -1 -1  1 -1  0  0  0  1]" : {-1: [(1, 2, 4), (0, 5, 8), (1, 5, 9)], 1: [(0, 3, 6)]},
	"[-1  0 -1  0  0 -1  1  0  0  0]" : {-1: [(1, 2, 6), (0, 5, 8)]},
	"[ 1  0 -1  0  0 -1  0  0  0  1]" : {-1: [(0, 9, 6)], 1: [(1, 9, 5)]},
	"[-1  0 -1 -1  0  1  0  0  0  1]" : {-1: [(0, 3, 6)], 1: [(1, 3, 5)]},
	"[-1  0  0 -1  1 -1 -1  0  0  0]" : {-1: [(0, 5, 8), (0, 6, 9)]},
	"[-1  0  0 -1  0  1 -1  0  0  0]" : {-1: [(1, 3, 5), (0, 6, 9)]},
	"[ 1  0  0 -1  0 -1 -1  1  0  0]" : {-1: [(0, 7, 4), (1, 7, 5)]},
	"[-1  0 -1 -1  0 -1  1  1  0  0]" : {-1: [(1, 2, 6), (0, 5, 8), (1, 5, 7)]},
	"[ 1  0 -1  0  0  1 -1  1  0  0]" : {-1: [(0, 7, 4)]},
	"[-1  0 -1  0  1 -1  0  0  0  0]" : {-1: [(1, 2, 4), (0, 5, 8)]},
	"[ 1  0 -1  0  0 -1  0  1  0  0]" : {-1: [(0, 7, 4)], 1: [(1, 7, 5)]},
	"[-1  0 -1 -1  0  1  0  1  0  0]" : {-1: [(0, 3, 6)], 1: [(1, 3, 5)]},
	"[ 1  0 -1 -1  0 -1  0  1  0  1]" : {-1: [(0, 7, 4), (1, 7, 5), (0, 9, 6), (1, 9, 5)]},
	"[ 1 -1 -1  0  0  1 -1  1  0  1]" : {1: [(1, 5, 1), (0, 7, 4)]},
	"[-1 -1 -1  0  1 -1  0  0  0  1]" : {-1: [(1, 2, 4), (0, 5, 8), (1, 5, 9)]},
	"[ 1  0 -1  0 -1  1  0  0  0  1]" : {-1: [(0, 9, 6)]},
	"[-1 -1 -1  0  0  1  0  0  0  1]" : {-1: [(0, 1, 4)], 1: [(1, 1, 5)]},
	"[-1 -1  0  0  1 -1 -1  0  0  0]" : {-1: [(0, 5, 8), (0, 6, 9)]},
	"[-1 -1  0  0  0  1 -1  0  0  0]" : {1: [(0, 1, 4)], -1: [(1, 1, 5), (0, 6, 9)]},
	"[ 1 -1  0  0  0 -1 -1  1  0  0]" : {-1: [(0, 7, 4), (1, 7, 5)]},
	"[-1 -1 -1  0  0 -1  1  1  0  0]" : {1: [(0, 1, 4)], -1: [(1, 2, 6), (0, 5, 8), (1, 5, 7)]},
	"[-1 -1 -1  0  0  1  0  1  0  0]" : {-1: [(0, 1, 4)], 1: [(1, 1, 5)]},
	"[ 1 -1 -1  0  0 -1  0  1  0  1]" : {-1: [(0, 7, 4), (1, 7, 5), (0, 9, 6), (1, 9, 5)]},
	"[-1 -1 -1 -1  0  1  0  1  0  1]" : {1: [(0, 1, 4), (0, 3, 6)], -1: [(1, 1, 5), (1, 3, 5)]},
	"[-1  0  0 -1  1  1  1  0  0  0]" : {1: [(1, 3, 5)]},
	"[ 1  0  0 -1  1 -1  1  1  0  0]" : {1: [(0, 4, 1), (1, 7, 5)]},
	"[ 1  0  0 -1  1  0 -1  1  0  0]" : {1: [(0, 4, 1)]},
	"[-1  0 -1 -1  1  0  1  1  0  0]" : {1: [(0, 2, 5), (1, 2, 6)], -1: [(1, 2, 4)]},
	"[ 1  0 -1 -1 -1  0  1  1  1  0]" : {1: [(1, 6, 2), (0, 8, 5)], -1: [(1, 8, 4)]},
	"[ 1  0  0 -1 -1  1  1  0  1  0]" : {1: [(0, 5, 2), (1, 5, 3), (1, 8, 4)]},
	"[ 1 -1  0  0  0 -1  1  0  1  0]" : {1: [(0, 6, 3)]},
	"[-1 -1  0 -1  0  1  1  0  1  0]" : {1: [(0, 1, 4), (1, 3, 5)], -1: [(1, 1, 5)]},
	"[ 1 -1  0 -1  0 -1  1  1  1  0]" : {1: [(0, 7, 4)], -1: [(1, 7, 5)]},
	"[-1 -1  0 -1  1  0 -1  0  1  0]" : {-1: [(0, 6, 9), (1, 6, 8)]},
	"[-1 -1  0 -1  0  1 -1  1  0  0]" : {1: [(0, 1, 4)], -1: [(1, 1, 5), (1, 3, 5), (0, 6, 9)]},
	"[-1 -1  0 -1  0  0  1  1  0  0]" : {-1: [(0, 1, 4)]},
	"[ 1 -1  0 -1  0  0 -1  1  1  0]" : {-1: [(0, 7, 4), (0, 8, 5), (1, 8, 6)]},
	"[-1 -1 -1 -1  0  0  1  1  1  0]" : {1: [(0, 1, 4), (0, 2, 5)], -1: [(1, 2, 6)]},
	"[ 1 -1 -1 -1  0  0  0  1  1  1]" : {-1: [(0, 7, 4), (0, 8, 5), (0, 9, 6)]},
}