import { Component, OnInit } from '@angular/core';
import { FocusService } from '../focus.service';
import { MatTableDataSource } from '@angular/material';


@Component({
  selector: 'app-pricelist',
  templateUrl: './pricelist.component.html',
  styleUrls: ['./pricelist.component.scss']
})
export class PricelistComponent implements OnInit {
  dataSource:any;
  constructor(private focusService: FocusService) {
    
   }

   displayedColumns = ['id', 'ListPrice' ,'DollarsOff', 'NetPrice', 'Off', 'HarmonyCost', 'CostConcession', 'SpecialCost', 'Comments']
  //  displayedColumns = ['ListPrice']

  ngOnInit() {
    this.PriceList();
  }

  data : any = [];
  PriceList(){
    this.focusService.PriceList().subscribe(
      response =>{
          this.data=response;
          console.log(this.data)
        }
    )}
}
