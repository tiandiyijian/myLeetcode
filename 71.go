package leetcode

import (
	"strings"
)

func simplifyPath(path string) string {
	dirs := []string{}
	for _, dir := range strings.Split(path, "/") {
		if dir == "/" || dir == "" || dir == "." {
			continue
		}
		if dir == ".." {
			if len(dirs) > 0 {
				dirs = dirs[:len(dirs)-1]
			}
			continue
		}
		dirs = append(dirs, dir)
	}
	return "/" + strings.Join(dirs, "/")
}
