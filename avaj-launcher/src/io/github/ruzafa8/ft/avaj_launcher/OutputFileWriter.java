package io.github.ruzafa8.ft.avaj_launcher;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class OutputFileWriter {
    private static final String filename = "simulation.txt";

    public static void write(String content) {
        try (BufferedWriter out = new BufferedWriter(new FileWriter(filename, true))) {
            out.write(content + "\n");
        } catch (IOException e) {
            System.err.println("Error writing to output file");
        }
    }
}
