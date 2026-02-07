# LC-733 Flood Fill

## 💡 Idea

DFS Basics :

explore the complete depth starting at a node or Use any other method but to practise DFS this question is good

## 💻 Code

```python
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] != color) {
            int ogcolor = image[sr][sc];
            dfs(sr, sc, color, ogcolor , image);
        }
        return image;

    }
    private static void dfs(int sr, int sc, int color, int ogcolor, int [][] image) {
        image[sr][sc] = color;

        if (sr - 1 > -1 && image[sr - 1][sc] == ogcolor) // up
        {
            dfs(sr - 1, sc, color, ogcolor , image);
        }
        if (sr + 1 < image.length && image[sr + 1][sc] == ogcolor) // down
        {
            dfs(sr + 1, sc, color, ogcolor , image);
        }
        if (sc + 1 < image[0].length && image[sr][sc + 1] == ogcolor) // right
        {
            dfs(sr, sc + 1, color, ogcolor , image);
        }
        if (sc - 1 > -1 && image[sr][sc - 1] == ogcolor) // left
        {
            dfs(sr, sc - 1, color, ogcolor , image) ;
        }
    }
}
```

