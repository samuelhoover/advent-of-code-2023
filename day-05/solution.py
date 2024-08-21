# pyright: basic

from collections.abc import Generator


with open(f"{input('example or input: ')}.txt", mode="r") as f:
    almanac: list[str] = f.read().strip().split("\n")


def get_maps(almanac) -> list[list[tuple[int, ...]]]:
    maps: list[list[tuple[int, ...]]] = []

    for i, line in enumerate(almanac[1:]):
        if line != "":
            try:
                dst, src, rangeLen = map(int, line.split())
                maps[-1].append((dst, src, rangeLen))
            except ValueError:
                continue
        else:
            maps.append([])

        maps[-1].sort(key=lambda x: x[1])

    for m in maps:
        for i, _ in enumerate(m[:-1]):
            if not m[i][1] + m[i][2] <= m[i + 1][1]:
                print(m[i], m[i + 1])

    return maps


def part1(almanac, maps) -> int:
    seeds: list[int] = list(map(int, almanac[0].split(" ")[1:]))
    locs: list[int] = []
    for x in seeds:
        for m in maps:
            for d, s, r in m:
                if x in range(s, s + r):
                    x: int = d + (x - s)
                    break

        locs.append(x)

    return min(locs)


def part2(almanac, maps) -> int:
    seeds_ranges: list[int] = list(map(int, almanac[0].split(" ")[1:]))
    seeds: list[tuple[int, int]] = [
        (seeds_ranges[i], seeds_ranges[i + 1]) for i in range(0, len(seeds_ranges), 2)
    ]

    def remap(lo, hi, m) -> Generator[tuple[int, int]]:
        ans: list[tuple[int, int, int]] = []
        for d, s, R in m:
            end: int = s + R - 1

            if not (end < lo or s > hi):
                ans.append((max(s, lo), min(end, hi), d - s))

        for i, interval in enumerate(ans):
            low, ran, D = interval
            yield (low + D, ran + D)

            if i < len(ans) - 1 and ans[i + 1][0] > ran + 1:
                yield (ran + 1, ans[i + 1][0] - 1)

        if len(ans) == 0:
            yield (lo, hi)
            return

        if ans[0][0] != lo:
            yield (lo, ans[0][0] - 1)

        if ans[-1][1] != hi:
            yield (ans[-1][1] + 1, hi)

    loc: int = 1 << 60

    for start, R in seeds:
        cur_intervals: list[tuple[int, int]] = [(start, start + R - 1)]
        new_intervals: list[tuple[int, int]] = []

        for m in maps:
            for lo, hi in cur_intervals:
                for new_interval in remap(lo, hi, m):
                    new_intervals.append(new_interval)

            cur_intervals, new_intervals = new_intervals, []

        for lo, _ in cur_intervals:
            loc = min(loc, lo)

    return loc


def main(almanac) -> None:
    maps: list[list[tuple[int, ...]]] = get_maps(almanac)
    print("Part 01:")
    print(f"Location: {part1(almanac, maps)}\n")
    print("Part 02:")
    print(f"Location: {part2(almanac, maps)}")


if __name__ == "__main__":
    main(almanac)
