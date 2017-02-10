#include <stdio.h>

int miro[1001][1001];
int ans[1001][1001];



int go(int a, int b){
	if (a==1 && b==1){
		//ans[a][b] = miro[a][b];
		return miro[a][b];
	}
	
	if( a==0 || b==0 ) return 0;
	
	
	if (ans[a][b] != 0){
		return ans[a][b];	
	}
	
	
	// if (a==1){
	// 	ans[a][b] = go(a, b-1) + miro[a][b];
	// 	return ans[a][b];
	// }
	
	// if (b==1){
	// 	ans[a][b] = go(a-1, b) + miro[a][b];
	// 	return ans[a][b];
	// }
	
	if( go(a-1, b) >= go(a, b-1) ){
		ans[a][b] = go(a-1, b) + miro[a][b];
	}
	else{
		ans[a][b] = go(a, b-1) + miro[a][b];
	}
	return ans[a][b];
		
}

int main()
{
	int m, n;
    scanf("%d %d", &m, &n);
	
	for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            scanf("%d", &miro[i][j]);
	
	printf("%d\n", go(m, n) );
    return 0;
}






























