import { Component, OnInit } from '@angular/core';
import { ContentService } from '../shared/services/content.service';
import { ActivatedRoute } from '@angular/router';
import { PageModel } from "src/models/PageModel";

@Component({
  selector: 'app-page',
  templateUrl: './page.component.html',
  styleUrls: ['./page.component.css']
})
export class PageComponent implements OnInit {
  page: PageModel;

  constructor(private route: ActivatedRoute,
              private contentService: ContentService) { }

  ngOnInit() {
    console.log(this.route);
    const pageData = this.route.snapshot.data['page'];
    console.log(pageData);
    this.page = this.contentService.pages.get(pageData);
    console.log(this.page);
    console.log(this.contentService.pages);
  }
}
