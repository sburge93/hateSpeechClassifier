import { Component, OnInit, OnDestroy } from '@angular/core';
import { HateSpeechApiService } from '../api.service/HateSpeechApiService';
import { MatCardModule } from '@angular/material/card';
import { Subscription } from 'rxjs';
import { TweetModel } from 'src/models/TweetModel';
import { Label, Color } from 'ng2-charts';
import { ChartDataSets } from 'chart.js';


@Component({
  selector: 'app-page',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.css']
})
export class GraphComponent implements OnInit, OnDestroy {
  hateSpeechModelSubs: Subscription;
  hateSpeechModel: TweetModel[];
  public chartLabels: Label[] = [];
  public chartData: ChartDataSets[] = [];
  public loaded: Boolean;

  constructor(private hatespeechApi: HateSpeechApiService) {
  }


  lineChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,255,0,0.28)',
    },
  ];
  chartOptions = {
    responsive: true
  };

  ngOnInit() {
    setTimeout(() => {
      this.getData();
    }, 5000);
  }

  getData() {
  this.hateSpeechModelSubs = this.hatespeechApi
    .getHateSpeech()
    .subscribe(res => {
      console.log(res)
      this.hateSpeechModel = res;
      this.chartLabels = this.hateSpeechModel.map(item => item.minute);
      this.chartData = [{ data: this.hateSpeechModel.map(item => item.count), label: 'Tweets' }];
      console.log(this.hateSpeechModel)
      this.loaded = true
    },
      console.error);
}

ngOnDestroy() {
  this.hateSpeechModelSubs.unsubscribe();
}
}