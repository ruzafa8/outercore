package io.github.ruzafa8.ft.avaj_launcher;

import java.io.IOException;
import java.io.PrintWriter;

public class OutputFileWriter {
    private static final String filename = "simulation.txt";
    private static final PrintWriter writer;

    static {
        try {
            writer = new PrintWriter(filename);
        } catch (IOException e) {
            throw new SimulationException("Error writing to output file: " + e.getMessage());
        }
    }

    public static void write(String content) {
        writer.println(content);
    }

    public static void close() {
        writer.flush();
        writer.close();
    }
}
