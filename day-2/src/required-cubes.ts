import { Cubes, readGamesFile } from './read-games-file'

export function requiredCubes(gamesFilePath: string): number {
	const games = readGamesFile(gamesFilePath)

	const gamePowers = games.map(game => {
		const maxCubes: Cubes = {
			'red': 0,
			'green': 0,
			'blue': 0
		}

		game?.forEach(cube => {
			const colour = cube[1]
			const number = Number(cube[0])

			if (number > maxCubes[colour]) {
				maxCubes[colour] = number
			}
		})

		return maxCubes.red * maxCubes.green * maxCubes.blue
	})

	return gamePowers.reduce((sum, power) => sum += power)
}

console.log(requiredCubes('./inputs/input.txt'))