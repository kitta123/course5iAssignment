import { Component, OnInit } from '@angular/core';
import { FocusService } from '../focus.service';
import { MatTableDataSource } from '@angular/material';
// import  *  as  data  from  './data.json';


@Component({
  selector: 'app-pricelist',
  templateUrl: './pricelist.component.html',
  styleUrls: ['./pricelist.component.scss']
})
export class PricelistComponent implements OnInit {
  dataSource:any;
  // products: any = (data as any).default;

  constructor(private focusService: FocusService) {
    
   }

   displayedColumns = ['id', 'ListPrice' ,'DollarsOff', 'NetPrice', 'Off', 'HarmonyCost', 'CostConcession', 'SpecialCost', 'Comments']

  ngOnInit() {
    this.PriceList();
    // console.log(data);
  }

  data : any = [];
  PriceList(){
    this.focusService.PriceList().subscribe(
      response =>{
          this.data=response;
          // console.log(this.data)
        }
    )}
}
