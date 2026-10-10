const { exec } = require('child_process');

exec('go run ~/app.go', (error, stdout, stderr) => {
    if (error) {
        console.error(`Ошибка запуска Go: ${error.message}`);
        return;
    }
    console.log(`[JS] Получил ответ: ${stdout.trim()}`);
});
