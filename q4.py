def flip_an_invert_image(matrix):
	n_row_sz = len(matrix)
	m_col_sz = len(matrix[0])
	for r in range(n_row_sz):
		for c in range((m_col_sz+1)//2):
			matrix[r][c], matrix[r][m_col_sz-1-c] = matrix[r][m_col_sz-1-c] ^ 1, matrix[r][c] ^ 1
	return matrix

def main():
    print(flip_an_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_an_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()