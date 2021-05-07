import { Injectable } from '@angular/core';
import { PageModel } from "src/models/PageModel";

@Injectable()
export class ContentService {

pages: Map<string, PageModel>
constructor() {
    let pagesMap = new Map<string, PageModel>();
  pagesMap.set("home", {
    title: "Home",
    subtitle: "Welcome to my final year development project!",
    content: "Click on about to find out more about this project or go to straight to the data page to see the classified data.",
    image: "./assets/bg03.jpg",
  });
  pagesMap.set("about", {
    title: "About",
    subtitle: "About This Project..",
    content: "This development project focuses on both machine learning and programming with the aim to create a hatespeech classifier that identifies hateful tweets with real time data streamed from twitter.",
    image: "./assets/bg02.jpg",
  });
  pagesMap.set("contact", {
    title: "Contact",
    subtitle: "Feel Free to Contact Me About This Project!",
    content: "ST20008817@outlook.cardiffmet.ac.uk",
    image: "./assets/bg01.jpg",
  });
  this.pages = pagesMap
  }

  
}