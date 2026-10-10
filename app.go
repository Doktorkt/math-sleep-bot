package main
import (
"fmt"
"os/exec"
)

func main() {
// Текст, который сгенерировал Go
secretMessage := "КВАНТОВЫЙ_КОМПЬЮТЕР"

// Go вызывает Python и передает ему этот текст
cmd := exec.Command("python", "/data/data/com.termux/files/home/processor.py", secretMessage)
out, _ := cmd.Output()

fmt.Print(string(out))
}
