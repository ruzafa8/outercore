package io.github.ruzafa8.ft.avaj_launcher;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class OutputFileWriter {
    private static final String filename = "simulation.txt";
    private static final StringBuilder builder = new StringBuilder();

    static {
        createOrEmptyOutputFile();
    }

    public static void write(String content) {
        builder.append(content).append("\n");
    }

    public static void flush() {
        try (BufferedWriter out = new BufferedWriter(new FileWriter(filename, true))) {
            out.write(builder.toString());
            builder.setLength(0);
        } catch (IOException e) {
            throw new SimulationException("Error writing to output file");
        }
    }

    public static void createOrEmptyOutputFile() {
        try {
            new PrintWriter(filename).close();
        } catch (IOException e) {
            throw new SimulationException("Error writing to output file");
        }
    }
}
