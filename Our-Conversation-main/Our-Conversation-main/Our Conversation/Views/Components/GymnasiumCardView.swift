//
//  FriendsCardView.swift
//  Our Conversation
//
//  Created by Emil Holmgaard on 15/02/2023.
//

import SwiftUI

struct GymnasiumCardView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Gymnasium")
                .font(.title3)
                .fontWeight(.semibold)
                .gradientForeground(colors: [.pink, .yellow])
                .multilineTextAlignment(.leading)
            Text("100 Spørgsmål")
                .fontWeight(.semibold)
                .gradientForeground(colors: [.pink, .yellow])
                .font(.footnote)
                .multilineTextAlignment(.leading)
            Text("At tale om gymnasiet fremmer akademisk forberedelse, karrie og livskompetencer")
                .fontWeight(.semibold)
                .gradientForeground(colors: [.pink, .yellow])
                .font(.body)
                .multilineTextAlignment(.leading)
        }
        .foregroundColor(Color.white)
        .padding(20)
        .frame(width: 252, height: 190)
        .background(Color(hue: 0.678, saturation: 0.0, brightness: 0.116))
        .cornerRadius(20)
    }
}

struct GymnasiumCardView_Previews: PreviewProvider {
    static var previews: some View {
        GymnasiumCardView()
    }
}
