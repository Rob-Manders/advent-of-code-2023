import * as fs from 'fs'

export type Cubes = { [index: string]: number }

export function readGamesFile(path: string) {
	const file = fs.readFileSync(path, 'utf-8')
	const lines = file.split('\n')
	
	const games = lines.map(line => {
		let cubesList = line.split(':').pop()?.split(/(,|;)/)

		cubesList = cubesList?.filter(element => {
			if (element != ',') {
				if (element != ';') return element
			}
		})

		const cubes = cubesList?.map(cubeString => {
			return cubeString.trimStart().split(' ')
		})

		return cubes
	})

	return games
}