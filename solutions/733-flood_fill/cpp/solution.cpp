/*
 * 733. Flood Fill
 * Author: Artur Gasparyan
 * Date: 16 Jan 2023
 * Link: https://leetcode.com/problems/flood-fill/submissions/879160016/
*/


using Coord = std::tuple<int, int>;

struct coordHash
{
    std::size_t operator()(const Coord& coord) const {
        return std::get<0>(coord) * 31 + std::get<1>(coord);
    }
};

const int rowJumps[4] = {-1, 1, 0, 0};
const int colJumps[4] = {0, 0, -1, 1};

class Solution {
public:
    Solution() {
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);
    }

    std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>>& image, int sr, int sc, int color) {
        std::stack<Coord> frontier;
        std::unordered_set<Coord, coordHash> visited;

        const auto m = image.size();
        const auto n = image[0].size();
        const auto startColor = image[sr][sc];

        frontier.emplace(sr, sc);

        while (!frontier.empty()){
            auto coord = frontier.top();
            frontier.pop();

            if (visited.find(coord) != visited.end())
                continue;

            const auto [row, col] = coord;
            visited.emplace(row, col);

            for (auto iJump = 0; iJump < 4; ++iJump) {
                const auto newRow = row + rowJumps[iJump];
                const auto newCol = col + colJumps[iJump];

                if (
                    newRow < 0 || newRow >= m ||
                    newCol < 0 || newCol >= n ||
                    image[newRow][newCol] != startColor
                )
                    continue;

                frontier.emplace(newRow, newCol);
            }

            image[row][col] = color;
        }

        return image;
    }
};