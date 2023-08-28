#include <stdio.h>
int n, visted[10], queue[10], i, j, array[10][10], front = -1, rear = -1, s;

void BFS(int s) { // Add the missing data type 'int' for the parameter
    rear = rear + 1;
    queue[rear] = s;
    visted[s] = 1;
    front = front + 1;
    while (!(front == -1)) {
        printf("hello\n");
        for (i = 0; i < n; i++) {
            if (array[s][i] && !visted[i]) {
                rear = rear + 1;
                queue[rear] = i;
                visted[i] = 1; // You should mark the node as visited here
            }
        }
        front = front + 1;
        if (front > rear) {
            front = rear = -1;
        }
        if (front <= rear) {
            s = queue[front];
        }
    }
}

int main() {
    printf("BFS using ARRAY\n");

    printf("Enter number of nodes: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d node connected to %d: ", i, j);
            scanf("%d", &array[i][j]);
        }
    }
    for (i = 0; i < n; i++) {
        queue[i] = 0;
        visted[i] = 0;
    }
    printf("\nThe graph is:\n ");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
    printf("\nEnter the starting node: ");
    scanf("%d", &s);
    BFS(s); // Call the function without 'void' and with the 's' argument
    printf("Queue: ");
    for (i = 0; i < n; i++) {
        printf("%d ", queue[i]);
    }
    printf("\nVisited: ");
    for (i = 0; i < n; i++) {
        printf("%d ", visted[i]);
    }
    return 0;
}
