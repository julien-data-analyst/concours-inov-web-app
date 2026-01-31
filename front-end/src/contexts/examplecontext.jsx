import { createContext, useState, useContext, useEffect } from "react";

const ExampleContext = createContext()

export const useExampleContext = () => useContext(ExampleContext)

export const ExampleProvider = () => {
    
}