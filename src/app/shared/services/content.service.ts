import { Injectable } from '@angular/core';
import { PageModel } from "src/models/PageModel";

@Injectable()
export class ContentService {

pages: Map<string, PageModel>
constructor() {
    let pagesMap = new Map<string, PageModel>();
  pagesMap.set("home", {
    title: "Home",
    subtitle: "Welcome Home!",
    content: "Some home content.",
    image: "./assets/bg03.jpg",
  });
  pagesMap.set("about", {
    title: "About",
    subtitle: "About Us",
    content: "Some content about us.",
    image: "./assets/bg02.jpg",
  });
  pagesMap.set("contact", {
    title: "Contact",
    subtitle: "Contact Us",
    content: "How to contact us.",
    image: "./assets/bg01.jpg",
  });
  this.pages = pagesMap
  }

  
}