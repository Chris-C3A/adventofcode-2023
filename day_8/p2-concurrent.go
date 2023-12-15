package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

var done = false

func main() {
	var input string

	// read from stdin
	reader := bufio.NewReader(os.Stdin)
	for {
		line, err := reader.ReadString('\n')

		if err != nil && err == io.EOF {
				break
		}

		if err != nil {
				fmt.Println(err)
				break
		}

		input = input + line
	}

	instructions, network := parseInput(input)

	// fmt.Println(instructions)
	// fmt.Println(network)

	// get keys that ends with A from network
	var startNodes []string

	for key := range network {
		if strings.HasSuffix(key, "A") {
			startNodes = append(startNodes, key)
		}
	}
	
	currentNodes := startNodes

	fmt.Println(currentNodes)


	// create an array for channels for each current node
	nextNodes := make([]chan string, len(currentNodes))
	for i := 0; i < len(currentNodes); i++ {
		// create a channel for each node of buffer 10
		// to store the next node of every step
		nextNodes[i] = make(chan string, 50)
	}

	for i := 0; i < len(currentNodes); i++ {
		go runInstructions(currentNodes[i], instructions, nextNodes[i], network)
	}

	steps := 0
	for !allNodesEnded(currentNodes) {
		// get next nodes from channels
		for i := 0; i < len(currentNodes); i++ {
			currentNodes[i] = <- nextNodes[i]
		}
		steps++
		// run instructions concurrently


		// for _, instruction := range instructions {
		// 	for i := 0; i < len(currentNodes); i++ {
		// 		go runInstructions(instruction)
		// 	}
		// 	// for i := 0; i < len(currentNodes); i++ {
		// 	// 	if instruction == 'L' {
		// 	// 		currentNodes[i] = network[currentNodes[i]][0]
		// 	// 	} else if instruction == 'R' {
		// 	// 		currentNodes[i] = network[currentNodes[i]][1]
		// 	// 	} else {
		// 	// 		fmt.Println("ERROR")
		// 	// 	}
		// 	// }
		// 	steps++
		// }
	}

	done = true

	fmt.Println(steps)
}

func parseInput(input string) (string, map[string][2]string) {
	var instructions string
	var network map[string][2]string

	parts := strings.Split(input, "\n\n")

	instructions = parts[0]
	rest := parts[1]

	// parse network
	network = make(map[string][2]string)
	for _, line := range strings.Split(rest, "\n") {
		// ignore empty lines
		if line == "" {
			continue
		}

		temp := strings.Split(line, " = ")

		node := temp[0]
		temp[1] = strings.Replace(temp[1], "(", "", -1)
		temp[1] = strings.Replace(temp[1], ")", "", -1)

		targets := strings.Split(temp[1], ", ")

		network[node] = [2]string(targets)
	}

	return instructions, network
}

func allNodesEnded(nodes []string) bool {
	for _, node := range nodes {
		if !strings.HasSuffix(node, "Z") {
			return false
		}
	}

	return true
}

func runInstructions(currentNode, instructions string, nextNodes chan string, network map[string][2]string) {
	// run forever until done
	var nextNode string
	for !done {
		for _, instruction := range instructions {
			if instruction == 'L' {
				nextNode = network[currentNode][0]
			} else if instruction == 'R' {
				nextNode = network[currentNode][1]
			} else {
				fmt.Println("ERROR")
			}
			nextNodes <- nextNode
			currentNode = nextNode
		} 
	}
}

