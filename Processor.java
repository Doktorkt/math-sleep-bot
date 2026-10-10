public class Processor {
    public static void main(String[] args) {
        // Проверяем, передали ли нам вообще хоть что-то
        if (args != null && args.length > 0) {
            String text = args[0].toUpperCase();
            System.out.println(text + " ⚡ [STATUS: QUANTUM COMPLETED]");
        } else {
            // Если аргумент потерялся в дороге, Java сама сгенерирует текст!
            System.out.println("РЕТЮЬПМОК_ЙЫВОТНАВК (Java сама взяла строку) ⚡ [STATUS: QUANTUM COMPLETED]");
        }
    }
}
