import { Cubes, readGamesFile } from "./read-games-file"

export function possibleGames(cubes: Cubes, gamesFilePath: string): number {
	const games = readGamesFile(gamesFilePath)

	let sumOfGames = 0

	games.forEach((game, index) => {
		let valid = true

		game?.forEach(cube => {
			const colour = cube[1]
			const number = Number(cube[0])

			if (number > cubes[colour]) valid = false
		})
		
		if (valid) sumOfGames += (index + 1)
	})

	return sumOfGames
}

const cubes = {
	'red': 12,
	'green': 13,
	'blue': 14
}

const result = possibleGames(cubes, './inputs/input.txt')

console.log(result)
