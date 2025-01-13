package io.github.ruzafa8.ft.avaj_launcher;

import io.github.ruzafa8.ft.avaj_launcher.flyable.AircraftFactory;
import io.github.ruzafa8.ft.avaj_launcher.flyable.Flyable;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Simulation {
    private static int numberOfSimulations;
    private static final WeatherTower weatherTower = new WeatherTower();

    public static void main(String[] args) {
        try {
            if (args.length != 1)
                throw new SimulationException("Usage: java Main <input file>");
            Simulation.parseFile(args[0]);
            Simulation.simulate();
            OutputFileWriter.flush();
            System.exit(0);
        } catch (SimulationException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }

    private static void simulate() {
        for (int i = 0; i < Simulation.numberOfSimulations; i++)
            Simulation.weatherTower.changeWeather();
    }

    private static void parseFile(String filename) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            Simulation.numberOfSimulations = Integer.parseInt(reader.readLine());
            if (Simulation.numberOfSimulations <= 0)
                throw new SimulationException("Number of simulations must be greater than 0");
            reader.lines().map(Simulation::parseLine).forEach(flyable -> flyable.registerTower(Simulation.weatherTower));
        } catch (NumberFormatException e) {
            throw new SimulationException("First line must be a valid number (the number of simulations)");
        } catch (FileNotFoundException e) {
            throw new SimulationException("File not found: " + filename);
        } catch (IOException e) {
            throw new SimulationException("I/O error: " + e.getMessage());
        }
    }

    private static Flyable parseLine(String line) {
        String[] tokens = line.split("\\s+");
        if (tokens.length != 5)
            throw new SimulationException("Invalid format at \"" + line + "\"");
        try {
            int longitude = Integer.parseInt(tokens[2]);
            int latitude = Integer.parseInt(tokens[3]);
            int height = Integer.parseInt(tokens[4]);
            if (longitude < 0 || latitude < 0 || height < 0)
                throw new SimulationException("Numbers must be positive at \"" + line + "\"");
            Coordinates coordinates = new Coordinates(longitude, latitude, height);
            return AircraftFactory.getInstance().newAircraft(tokens[0], tokens[1], coordinates);
        } catch (NumberFormatException e) {
            throw new SimulationException("Not a number at \"" + line + "\"");
        }
    }
}
